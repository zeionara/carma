from sys import argv
from os import path

from pandas import read_csv
from tqdm import tqdm

from cloud_mail_api import CloudMail

USERNAME = argv[1]
PASSWORD = argv[2]
ROOT = argv[3]

cm = CloudMail(USERNAME, PASSWORD)
cm.auth()

# print(cm.api.folder(ROOT))

df = read_csv('anecdotes.tsv', sep = '\t')

with tqdm(total = 9000) as pbar:
    for _, row in df.iloc[:9000].iterrows():
        filepath = path.join(ROOT, f'{row["id"]:08d}.mp3')
        filename = f'{row["id"]:08d}.{row["source"]}.mp3'

        cm.api.file.rename(
            filepath,
            filename
        )

        pbar.update()

    # print(filepath, filename)

# print(
#     cm.api.file.rename(
#         f'{ROOT}/00241247.mp3',
#         '00241247.aneks.mp3'
#     )
# )
