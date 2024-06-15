# DS
import os
from collections import defaultdict 
reg_amount = r'(\b\w+\b.*?\b\w+\b.*?) καθίσταται'
reg_contract = r"τη με αριθμό\s+(\w+)\s+σύμβαση|Σύμβαση"
global_errors = {}
contents_dict = {}
amounts_dict = {}
non_found = []
error_counter = 0
production_dir = r"C:\Users\pallist\Desktop\ΤΡΕΧΟΝΤΑ\1) Projects\Fix exodika\PRODUCTION - 11_6_ bup"
first_level_folders = [folder for folder in next(os.walk(production_dir))[1]]
errors = []
non_docs= []
non_word_document_types = ['docx','doc','odt','odf','xls', 'xlsx', 'db', 'pdf','ink','tmp','lnk']


def create_lists(n):
    return [[] for _ in range(n)]

init_list = create_lists(4)
errors_dict = defaultdict(lambda: init_list)


production_folders = [folder for folder in os.listdir(production_dir) if os.path.isdir(os.path.join(production_dir, folder)) and os.listdir(os.path.join(production_dir, folder))]

non_frontier_folders = [folder for folder in production_folders if 'non' in folder.lower()]
frontier_folders = [folder for folder in production_folders if 'frontier' in folder.lower() and 'non' not in folder.lower()]
mirror_folders = [folder for folder in production_folders if 'mirror' in folder.lower()]
erb_folders = [folder for folder in production_folders if 'erb' in folder.lower()]
heliopolis_folders = [folder for folder in production_folders if 'heliopolis' in folder.lower()]    
pillar_folders = [folder for folder in production_folders if 'pillar' in folder.lower()]
rest_do_value_folders = ['DoValue 13_5_24', 'Recovery 17_10_23','ΕΞΩΔΙΚΑ ΜΕΤΕΞΕΛΙΞΗ 26_11']

