# imprt the
import psycopg

from config.settings import Config

class Database:
    """
    Use singleton pattern to manage the PostgreSQL connection.
    
    Attributes:
        _instance: singleton instacne of the class
    """
    
    _instance = None
    
    def _init_(self):
        try:
            self._instance = psycopg.connect(
                user = Config.DB_USER,
                password = Config.DB_PASSWORD,
                host = Config.DB_HOST,
                port = Config.DB_PORT,
                dbname = Config.DB_NAME
            )
            
            # Display message -> debug
            print("Database connection established")
            
        except Exception as e:
            print(f"Error: {e}")
            
            
    @classmethod
    def _get_instance(cls):
        """private method that manages the singleton instance -> internally
        
        Return:
            Database connection: singleton instance 
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def _close_connection(self):
        if self._instance:
            self._instance.close()
            print("Connection closed")
            
# to improve the security we are goung to create two more methods:

def get_db():
    return Database._get_instance()._instance

def close_db():
    if Database._instance:
        Database._instance._close_connection()
        Database._instance = None
        