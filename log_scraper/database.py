import os
import pickle
from argparse import ArgumentParser
from warnings import warn


def parse_args():
    argparser = ArgumentParser()
    argparser.add_argument('db_path')

    return argparser.parse_args()


class ReplayDatabase:
    def __init__(self, file_name):
        self.file_name = file_name
        self.db = {}
        if os.path.exists(file_name):
            file = open(file_name, "rb")
            self.db = pickle.load(file)
            file.close()
        else:
            with open(file_name, "wb") as file:
                pickle.dump(self.db, file)

    def check_replay_exists(self, replay_id):
        return replay_id in self.db.keys()

    def get_replay(self, replay_id):
        return self.db[replay_id]

    def add_replay(self, replay_id, battle_log):
        self.db[replay_id] = battle_log

    def commit(self):
        with open(self.file_name, "wb") as file:
            pickle.dump(self.db, file)

    def close(self):
        warn("Deprecated method")


if __name__ == "__main__":
    database = ReplayDatabase(input("File name: "))
    db = database.db
    for x in db:
        print(f"=== START {x} ===")
        print(db[x])
    # args = parse_args()
    # r = ReplayDatabase(args.db_path)
