#-*-coding:utf-8 -*

class Recompositions:
    def __init__(self):
        self.recompositions_list=[]

    def recompose(self,substitutes_instance, categories_instance, products_instance):
        for substitute in substitutes_instance.substitutes_registered_list:
            recomposed_object = {}
            product_product_id = [product.id_product for product in\
            products_instance.products_list if product.id_product ==\
            substitute.product_product_id]
            substitute_product_id = [product.id_product for product in\
            products_instance.products_list if product.id_product ==\
            substitute.substitute_product_id]

            print (product_product_id, " - ",substitute_product_id)
            


            # for product in products_instance.products_list:


            #     if product.id_product == substitute.product_product_id:
            #         recomposed_object["product_product_id"] = product.id_product
            #         recomposed_object["product_product_name"] = product.product_name
            #         recomposed_object["product_nutriscore_grade"] = product.nutriscore_grade
            #         recomposed_object["product_url"] = product.url
            #         recomposed_object["product_stores"] = product.stores
            #         # print ("initial :", recompose_product_name)

            #     elif product.id_product == substitute.substitute_product_id:
            #         recomposed_object["substitute_product_id"] = product.id_product
            #         recomposed_object["substitute_product_name"] = product.product_name
            #         recomposed_object["substitute_nutriscore_grade"] = product.nutriscore_grade
            #         recomposed_object["substitute_url"] = product.url
            #         recomposed_object["substitute_stores"] = product.stores  
            #         # print ("substitute :", recompose_product_name)

            # for key, value in recomposed_object.items():
            #     product_category_id = 
            #     if key == "initial_name":
            #         print ("initial_name: ", value,)
            #     elif key == "substitute_name":
            #         print ("substitute_name: ", value)