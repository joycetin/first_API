from flask import Flask, jsonify

#this is an instance
app=Flask(__name__)

#creating a route
@app.route("/articles")

#defining a function
def gettingArticles():                            
    articles = {
        "article1":{"Id":1,
                    "Title":'Web development',
                    "Body":' Web development refers to the creating, building, and maintaining of websites.',
                    "Author":'Nganda Gladys'
                    },

        "article2":{"Id":2,
                    "Title":'Graphics Design',
                    "Body":'Graphic design is a craft where professionals create visual content to communicate messages.',
                    "Author":'Abbo Mary'
                    },

        "article2":{"Id":3,
                    "Title":'Computer Hardware',
                    "Body":'Hardware refers to the computer\'s tangible components or delivery systems that store and run the written instructions provided by the software.',
                    "Author":'Atim Karen'
                    },

        "article1":{"Id":4,
                    "Title":'Database',
                    "Body":'In computing, a database is an organized collection of data stored and accessed electronically.',
                    "Author":'Hum Kay'
                    },

        "article2":{"Id":5,
                    "Title":'Restful APIs',
                    "Body":'Restful API is an interface that two computer systems use to exchange information securely over the internet.',
                    "Author":'Enoch Dammy'
                    }
    }

    return jsonify(articles)


if __name__=='main':
    app.run(debug=True)