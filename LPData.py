
from google.appengine.ext import db

class Lugger(db.Model):
    user = db.UserProperty()
    voted = db.BooleanProperty()
    votes = db.ListProperty(int)
    
class Totals(db.Model):
    shirts = db.ListProperty(int)
    votes = db.ListProperty(int)
    
    
T_Shirts = [
            (46 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/503000#entry-46"),
            (27 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/312359#entry-27"),
            (28 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/530113#entry-28"),
            (29 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/529868#entry-29"),
            (30 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/521110#entry-30"),
            (31 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/392986#entry-31"),
            (39 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/392986#entry-39"),
            (33 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/384274#entry-33"),
            (34 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/529602#entry-34"),
            (35 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/526344#entry-35"),
            (36 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/526344#entry-36"),
            (37 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/425298#entry-37"),
            (38 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/425298#entry-38"),
            (43 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/529634#entry-43"),
            (44 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/432199#entry-44"),
            (45 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/432199#entry-45"),
            (4  , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/525338#entry-4"),
            (5  , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/525338#entry-5"),
            (14 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/525338#entry-14"),
            (15 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/525338#entry-15"),
            (16 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/525338#entry-16"),
            (17 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/525338#entry-17"),
            (21 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/525338#entry-21"),
            (22 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/525338#entry-22"),
            (23 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/525338#entry-23"),
            (24 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/525338#entry-24"),
            (25 , "http://99designs.com/t-shirt-design/contests/open-source-t-shirt-design-67687/designers/527893#entry-25")
            ]
