import psutil
import os
import win32serviceutil
#Python 2.7
services = ['MSSQL$SQLEXPRESS', 'SQLTELEMETRY$SQLEXPRESS', 'MySQL80']

def getService(name):
    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()

    except Exception as ex:
        print(str(ex))
    return service


def Stop(services):
    services = services
    x = 0
    while (x <= len(services) - 1):
        service = getService(services[x])
        print services[x]
        if service:
            print("service found")
            if service and service['status'] == 'running':
                print("service is running")
                win32serviceutil.StopService(services[x])
                print '{} stopped'.format(services[x])
            else:
                print("service is not running")
        else:
            print("service not found")


        print "-----------------------------------------------"
        x = x + 1

def Start(services):
    services = services
    x = 0
    while (x <= len(services) - 1):
        service = getService(services[x])
        print services[x]
        if service:
            print("service found")
            if service and service['status'] == 'running':
                print("service is running")
            else:
                print("service is not running")
                win32serviceutil.StartService(services[x])
                print '{} started'.format(services[x])
        else:
            print("service not found")


        print "-----------------------------------------------"
        x = x + 1


print "Program start/stop services"
print "----------------------------------------------------------------------"
print "Start || Stop"
resposta = raw_input()

if (resposta.upper() == "START"):
    Start(services)
if (resposta.upper() == "STOP"):
    Stop(services)

raw_input("Press enter")
quit(0)
