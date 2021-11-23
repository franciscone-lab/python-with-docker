import psutil
import time
from connectdb import *

print('='*10,'INÍCIO DAS MEDIÇÕES','='*10)
print('-'*10,'Ctrl+C para parar','-'*10,'\n')

try:
    
    vetMem = []
    vetCpu = []
    vetDisc = []
    server_id = 0

    while True:
        server_id += 1

        if(server_id==1):

            mem_used = (psutil.virtual_memory().percent)
            cpu_used = (psutil.cpu_percent())
            disc_used = (psutil.disk_usage("/")).percent

            vetMem.append(float('{0:.2f}'.format(mem_used)))
            vetCpu.append(float('{0:.2f}'.format(cpu_used)))
            vetDisc.append(float('{0:.2f}'.format(disc_used)))
            
            data_hora = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
            print("Memória:",float('{0:.2f}'.format(mem_used)),"  | Data:",data_hora)
            print("CPU:",float('{0:.2f}'.format(cpu_used)),"       | Data:",data_hora)
            print("Disco:",float('{0:.2f}'.format(disc_used)),"    | Data:",data_hora)
            print("===============================================")
            time.sleep(2)
            
            insert_db(cpu_used, mem_used, disc_used, server_id)
        
        elif(server_id==2):
        # Funções de 1º Grau (f(x) = ax + b)
            mem_used2 = mem_used * 0.1
            cpu_used2 = cpu_used * 0.95
            disc_used2 = disc_used * 0.05

            vetMem.append(float('{0:.2f}'.format(mem_used2)))
            vetCpu.append(float('{0:.2f}'.format(cpu_used2)))
            vetDisc.append(float('{0:.2f}'.format(disc_used2)))
            
            data_hora = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
            print("Memória:",float('{0:.2f}'.format(mem_used2)),"  | Data:",data_hora)
            print("CPU:",float('{0:.2f}'.format(cpu_used2)),"       | Data:",data_hora)
            print("Disco:",float('{0:.2f}'.format(disc_used2)),"    | Data:",data_hora)
            print("===============================================")
            time.sleep(2)
            
            insert_db(cpu_used2, mem_used2, disc_used2, server_id)


        elif(server_id==3):

            mem_used3 = mem_used * 0.3
            cpu_used3 = cpu_used * 0.55
            disc_used3 = disc_used * 0.15

            vetMem.append(float('{0:.2f}'.format(mem_used3)))
            vetCpu.append(float('{0:.2f}'.format(cpu_used3)))
            vetDisc.append(float('{0:.2f}'.format(disc_used3)))
            
            data_hora = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
            print("Memória:",float('{0:.2f}'.format(mem_used3)),"  | Data:",data_hora)
            print("CPU:",float('{0:.2f}'.format(cpu_used3)),"       | Data:",data_hora)
            print("Disco:",float('{0:.2f}'.format(disc_used3)),"    | Data:",data_hora)
            print("===============================================")
            time.sleep(2)
            
            insert_db(cpu_used3, mem_used3, disc_used3, server_id)
            server_id = 0
      
           
    
    
except KeyboardInterrupt:
    pass



