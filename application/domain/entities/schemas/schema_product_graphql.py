import strawberry

@strawberry.type
class ProductGraphQl:

    id : int
    name : str
    categorie : str
    price : int