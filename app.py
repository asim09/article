
from flask import Flask,jsonify,request
from utility import db_connection
import json,helpers
import helpers
from log import Log
import datetime

app = Flask(__name__)


@app.route('/api/create-article',methods=['POST'])
def create_article():
    
    '''
    This function will create article.
    '''
    data = request.get_json()
    author = data.get('author',None)
    title = data.get('title',None)
    description = data.get('description',None)
    tags = data.get('tags',None)
    response = None

    if author is not None and title is not None and tags is not None and description is not None:
        if (len(author) != 0 and len(title) != 0 and len(tags) != 0 and len(description) != 0):
            
            conn = db_connection()
            cursor = conn.cursor()
            try:
                sql = "select title from article where title = %s"  # This query will check if the article already exist.
                info = (title,)
                response = cursor.execute(sql,info)
                title_data = len(cursor.fetchall())
                if title_data:
                    return jsonify({'success':False,'message':"Article title already exist"})

                
            except Exception as e:
                helpers.getErrorLine()
                Log.log_error(e)
                cursor.close()
                conn.close()
                return jsonify({'success':False,'message':"Some Error Occured.Please Try again later"})

            try:
                sql = """INSERT into article (title,description,author) values(%s,%s,%s)"""
                info = (title,description,author)
                response = cursor.execute(sql,info)
                
                conn.commit()
                
            except Exception as e:
                helpers.getErrorLine()
                Log.log_error(e)
                cursor.close()
                conn.close()

            if response:
                article_id = cursor.lastrowid
                tag_data = [(article_id,obj) for obj in tags]

                try:
                    sql2 = "INSERT INTO tags (article_id,tag) VALUES (%s, %s)"
                    cursor.executemany(sql2, tag_data)
                    conn.commit()
                except Exception as e:
                    helpers.getErrorLine()
                    Log.log_error(e)
                cursor.close()
                conn.close()
            return jsonify({'success':True,'message':"Hurray! you have created article successfully!"})
        return jsonify({'success':False,'message':"Some Param is empty"})
    return jsonify({'success':False,'message':"Some Param is missing"})




@app.route('/api/list-article',methods=['GET'])
def list_article():
    
    '''
    This function will fetch article list.
    '''
    conn = db_connection()
    cursor = conn.cursor()
    try:
        sql = "select distinct id,title,description,author from article where soft_delete = 0"
        response = cursor.execute(sql)
        title_data = list(cursor.fetchall())
        titles = [x['id'] for x in title_data]
        temp_list = []

        for i in title_data:
            sql2 = "select t.tag from article as a inner join tags as t on a.id = t.article_id where a.id = '"+str(i['id'])+"'"
            response = cursor.execute(sql2)
            tag_data = cursor.fetchall()
            tag_list = [x['tag'] for x in tag_data]
            i['tags'] = tag_list

    except Exception as e:
        helpers.getErrorLine()
        Log.log_error(e)
        cursor.close()
        conn.close()
        return jsonify({'success':False,'message':"Some Error Occured.Please Try again later"})
    return jsonify({'success':True,'message':title_data})



@app.route('/api/delete-article',methods=['DELETE'])
def delete_article():
    data = request.get_json()
    id = data.get('id',None)

    if isinstance(id,int):
        conn = db_connection()
        cursor = conn.cursor()
        try:
            sql = "UPDATE article set soft_delete = 1 where id = %s"
            info = (id,)
            response = cursor.execute(sql,info)
            conn.commit()
            if response:
                return jsonify({'success':True, 'message':"article with id: " +str(id) + " is deleted successfully" })
            return jsonify({'success':False, 'message':"Please Try again" })
        except Exception as e:
            helpers.getErrorLine()
            Log.log_error(e)
        cursor.close()
        conn.close()
    return jsonify({'success':False, 'message':"Please Enter valid article ID" })


@app.route('/api/update-article',methods=['PUT'])
def update_article():
    
    '''
    This function will update single article along with its respective tags.
    '''

    data = request.get_json()

    article_id = data.get('id',None)
    author = data.get('author',None)
    title = data.get('title',None)
    description = data.get('description',None)
    tags = data.get('tags',None)


    conn = db_connection()
    cursor = conn.cursor()
    try:
        sql = "update article set author = %s,title = %s,description = %s where id = %s"  # This query will check if the article already exist.
        info = (author,title,description,article_id)
        response = cursor.execute(sql,info)
        conn.commit()

        if len(tags) > 0:
            id = article_id
            for obj in tags:
                sql2 = "UPDATE tags set tag = %s where article_id = %s"
                cursor.execute(sql2,(obj,id))
                response = cursor.execute(sql,info)
                conn.commit()
    except Exception as e:
        helpers.getErrorLine()
        Log.log_error(e)
        cursor.close()
        conn.close()
        return jsonify({'success':False, 'message':"Please update" })
    return jsonify({'success':True, 'message':"Data Updated Successfully!" })
    cursor.close()
    conn.close()




if __name__ == "__main__":
    app.debug = True
    app.run()
    # app.run(host="0.0.0.0", debug=True)
