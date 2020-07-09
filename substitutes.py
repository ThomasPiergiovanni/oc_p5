#-*-coding:utf-8 -*

import substitute

class Substitutes:
    def __init__(self):
        self.substitutes_proposed_list=[]
        self.substitutes_proposed_with_rank=[]
        self.selected_substitute = 0
        self.registration = False
        self.substitutes_registered_list=[]

    def instanciate_substitute(self, database_instance):
        database_instance.cursor.execute ("SELECT * FROM p5.substitute")
        selection = database_instance.cursor.fetchall()
        for elt in selection:
            product_product_id= elt[0]
            substitute_product_id = elt[1]
            substitute_instance = substitute.Substitute(product_product_id,\
            substitute_product_id)
            self.substitutes_registered_list.append(substitute_instance)

    def filter(self, product_instance):
        selected_product_nutriscore = [elt.nutriscore_grade for elt in\
        product_instance.selected_products if elt.id_product ==\
        product_instance.selected_product]
        selected_product_nutriscore = selected_product_nutriscore [0]
        for elt in product_instance.selected_products:
            if elt.id_product != product_instance.selected_product and\
            elt.nutriscore_grade < selected_product_nutriscore:
                self.substitutes_proposed_list.append(elt)

    def show_proposed(self):
        print ("SUBSTITUTES:")
        sorted_substitutes = sorted(self.substitutes_proposed_list, key = lambda \
        product : product.nutriscore_grade)
        rank = 1
        for elt in sorted_substitutes:
            print (rank ," - ",elt.product_name, " - ", elt.nutriscore_grade)
            substitutes_proposed_with_rank=(elt.id_product,\
            elt.product_name, elt.nutriscore_grade, rank)
            self.substitutes__proposed_with_rank.append(substitutes__proposed_with_rank)
            rank += 1

    def select(self):
        question= input("Which substitute you want to choose ?")
        question = int(question)
        for elt in self.substitutes_proposed_with_rank:
            if elt[3] == question:
                print ("You\'ve choosen the ", elt[1], "product as a substitute") 
                self.selected_substitute = elt[0]

    def register(self):
        question= input("Do you want to register that choice (y/n)?")
        question = str(question)
        if question in "yY":
            self.registration = True
            print("Substitute product has been registered !") 
        elif question not in "nN":
            print ("Only letter y/n can be used. Retry ")
            Substitutes.register(self)

    def recompose(self, categories_instance, products_instance):
        for substitute in self.substitutes_registered_list:
            for product in products_instance.products_list:
                if product.id_product == substitute.product_product_id:
                    print (substitute.product_product_id, " - ",\
            product.id_product, " - ", product.product_name)

    # def show_registered(self):
    #     print ("REGISTERED SUBSTITUTES:")
    #     sorted_substitutes = sorted(self.substitutes_registered_list, key = lambda \
    #     product : product.nutriscore_grade)
    #     rank = 1
    #     for elt in sorted_substitutes:
    #         print (rank ," - ",elt.product_name, " - ", elt.nutriscore_grade)
    #         substitutes_proposed_with_rank=(elt.id_product,\
    #         elt.product_name, elt.nutriscore_grade, rank)
    #         self.substitutes__proposed_with_rank.append(substitutes__proposed_with_rank)
    #         rank += 1


