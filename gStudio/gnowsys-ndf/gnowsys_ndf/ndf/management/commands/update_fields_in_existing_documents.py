''' imports from installed packages '''
from django.core.management.base import BaseCommand, CommandError

from django_mongokit import get_database

try:
    from bson import ObjectId
except ImportError:  # old pymongo
    from pymongo.objectid import ObjectId

''' imports from application folders/files '''
from gnowsys_ndf.ndf.models import Node

####################################################################################################################

class Command(BaseCommand):
    """This update-script updates fields' data-types or their values.
    """

    help = "\tThis update-script updates fields' data-types or their values."

    def handle(self, *args, **options):
        
        collection = get_database()[Node.collection_name]

        # Renames field: 'modified_by' to 'contributors'
        collection.update({'modified_by': {'$exists': True}}, {'$rename': {'modified_by': "contributors"}}, upsert=False, multi=True)

        # Updates location fields' values from '{}' (empty dictionary) to '[]' (empty list)
        collection.update({'location': {}}, {'$set': {'location': []}}, upsert=False, multi=True)
        

        # --- End of handle() ---

