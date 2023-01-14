from abc import ABC, abstractmethod

class ProductsBusinessLogic(ABC):

    @abstractmethod
    def get_response_format(self, data, offset: int = 0, limit: int = 100, page_number : int = 1, page_size : int = 10):
        pass