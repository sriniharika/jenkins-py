# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 13:17:47 2021

@author: NiharikaSrivastava

pip3 install flask

"""

from flask import Flask,jsonify,request,Response,make_response

from flask_sqlalchemy import SQLAlchemy

from marshmallow_sqlalchemy import ModelSchema

from marshmallow import fields

#from flask_sqlalchemy import relationship,ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3306/devops'
db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__='pythonproducts'
    productId = db.Column(db.Integer,primary_key=True)
    productName = db.Column(db.String(40))
    description = db.Column(db.String(60))
    productCode = db.Column(db.String(60))
    price = db.Column(db.Float)
    starRating = db.Column(db.Float)
    imageUrl = db.Column(db.String(40))
    reviews = db.relationship('Review',backref='pythonproducts',lazy=True)
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    def __init__(self,productName,description,productCode,price,starRating,imageUrl):
        self.productName = productName
        self.description = description
        self.productCode = productCode
        self.price = price
        self.starRating = starRating
        self.imageUrl = imageUrl
    def __repr__(self):
        return "%self.productId"
    
    
class Review(db.Model):
    __tablename__='Review'
    product_Id =  db.Column(db.Integer,primary_key=True)
    details =  db.Column(db.String(60))
    product_id = db.Column(db.Integer,db.ForeignKey('pythonproducts.productId'),nullable=False)
    
db.create_all()
class ProductSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Product
        sqla_session=db.session
    productId = fields.Number(dump_only = True)
    productName = fields.String(required = True)
    description = fields.String(required = True)
    productCode = fields.String(required = True)
    price = fields.Number(required = True)
    starRating = fields.Number(required = True)
    imageUrl = fields.String(required = True)


@app.route('/products',methods=['POST'])
def createProduct():    
    product_schema = ProductSchema()
    product = product_schema.load(request.get_json()) 
    return make_response(jsonify({"products":product_schema.dump(product.create())}),200)



@app.route('/products',methods=['GET'])
def getAllProducts():  
    get_products = Product.query.all()
    product_schema = ProductSchema(many = True)
    products = product_schema.dump(get_products)
    return make_response(jsonify({"products":products}),200)



#select * from pythonproducts where id =?
@app.route('/products/<int:productId>',methods=['GET'])
def getProductById(productId):  
    get_product = Product.query.get(productId)
    product_schema = ProductSchema()
    product = product_schema.dump(get_product)
    return make_response(jsonify({"products":product}),200)


@app.route('/products/<string:productName>',methods=['GET'])
def getProductByName(productName):  
    get_product = Product.query.filter_by(productName=productName)
    product_schema = ProductSchema(many = True)
    product = product_schema.dump(get_product)
    return make_response(jsonify({"products":product}),200)


@app.route('/products/<int:productId>',methods=['PUT'])
def updateProduct(productId):    
    
    get_product = Product.query.get(productId)
    #product = product_schema.load(request.get_json()) 
    data = request.get_json()
    if data.get('price'):
        get_product.price = data['price']
    db.session.add(get_product)
    db.session.commit()    
    product_schema = ProductSchema(only=['productId','price'])
    result = product_schema.dump(get_product)
    
    return make_response(jsonify({"products":result}),200)


@app.route('/products/<int:productId>',methods=['DELETE'])
def deleteProductById(productId):  
    get_product = Product.query.get(productId)
    db.session.delete(get_product)
    db.session.commit()
    return make_response(jsonify({"result":"product deleted"}),200)


app.run(port=8090)
print("server running")


#get_products = Product.query.all()
#product_schema = ProductSchema(many = True)


#products = product_schema.dump(get_products)
#print(products)


#select * from pythonproducts where productid=1
"""
get_product = Product.query.get(1)
product_schema = ProductSchema()


product = product_schema.dump(get_product)
print(product)

#select * from pythonproducts where productName='Iphone'
get_products = Product.query.filter_by(productName='Iphone12')
product_schema = ProductSchema(many = True)


products = product_schema.dump(get_products)
print(products)


"""














        
    
    
    
        
        
        
        
        
        
        
        

        
        
        
        
        
        
    
   
    
   
    
   
    
   
    