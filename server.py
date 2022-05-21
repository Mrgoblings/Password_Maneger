from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
import json

from dbconn import DataBase


app = Flask(__name__)
api = Api(app)

db = DataBase("localhost", "root", "", "passwordManager")

put_args = reqparse.RequestParser()

# "help" is the default value
put_args.add_argument("sait", type=str, required=True)
put_args.add_argument("login_name", type=str, required=True)
put_args.add_argument("password", type=str, required=True)
# put_args.add_argument("new_password", type=str, required=False)

patch_args = reqparse.RequestParser()
patch_args.add_argument("sait", type=str, required=True)
patch_args.add_argument("login_name", type=str, required=True)
patch_args.add_argument("password", type=str, required=True)
patch_args.add_argument("which_attribute", type=str, required=True)
patch_args.add_argument("updated_attribute", type=str, required=True)


class RestApi(Resource):
    # noinspection PyMethodMayBeStatic
    def get(self, acc_mail):
        accounts = db.get_all_passwords_for_user(acc_mail)
        if len(accounts) == 0:
            abort(404, message="The User doesn't exist or he doesn't have any passwords saved")

        return accounts, 200  # OK

    def post(self, acc_mail):
        args = put_args.parse_args()

        try:
            if not self.check_if_args_in_acc(acc_mail, args):
                return db.insert_password(acc_mail, args["sait"], args["login_name"], args["password"])
            else:
                abort(409, message="This user, mail and password already exist!")
        except KeyError as e:
            # The account doesn't exist in here
            print(e)
            return 409  # conflict

    def delete(self, acc_mail):
        args = {}

        try:
            args = json.loads(list(request.args)[0])
            print(f"{args}, {acc_mail}")
        except IndexError as e:
            abort(400, message=e)

        if "login_name" not in str(args) and "sait" not in str(args):
            abort(400, message="args doesn't contain 'login_name' and 'sait' in it")

        if self.check_if_args_in_acc(acc_mail, args):
            return db.delete_password(acc_mail, args["sait"], args["login_name"])

        abort(404, message="did not find the password in the database")  # not found

    def patch(self, acc_mail):
        args = {}
        try:
            args = patch_args.parse_args()
        except Exception as e:
            print(e)

        return db.edit_password(acc_mail, args["sait"], args["login_name"], args["password"], args["which_attribute"], args["updated_attribute"])

    @staticmethod
    def check_if_args_in_acc(acc_mail, args):
        return (args["sait"], args["login_name"], args["password"]) in db.get_all_passwords_for_user(acc_mail)


api.add_resource(RestApi, "/api/<string:acc_mail>", endpoint="api/")

if __name__ == "__main__":
    app.run(debug=True)

# https://www.tutorialspoint.com/http/http_status_codes.htm
# https://restfulapi.net/http-methods/#delete
# https://docs.python.org/3/library/stdtypes.html#frozenset.difference
