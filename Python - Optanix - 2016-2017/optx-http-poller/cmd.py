import argparse
import os

parser = argparse.ArgumentParser(description='Optanix HTTP poller')
parser.add_argument('-d', '--dev', default=False, action='store_true', help='run in dev mode')
parser.add_argument('-r', '--requirements', default=False, action='store_true', help='Install requirements')
parser.add_argument('-t', '--tests', default=False, action='store_true', help='run UnitTests') #remove action when find way to run unittests on test folder
parser.add_argument('-s', '--serve', default=False, action='store_true', help='run server')
parser.add_argument('-p', '--port', default=False, help='run server on special port')
parser.add_argument('-C', '--consumer', default=False, action='store_true', help='run consumer')
args = parser.parse_args()

runCommand = "python3 app.py "
if args.dev:
    runCommand += "--env=dev "
if args.port:
    runCommand += "--port={}".format(args.port)

if args.tests:
    os.system("python3 -m tornado.test.runtests tests.HomeHandlerTest")
elif args.requirements:
    os.system("pip3 install -r requirements.txt")
elif args.consumer:
    os.system("python3 -m consumer.py")
else:
    os.system(runCommand)
