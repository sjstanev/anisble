shutdown -r now
sudo shutdown -h now
su
ping 10.81.0.61
ping 10.81.0.62
ping 10.81.0.63
ping 10.81.0.64
ping 10.81.0.63
ip a
ls
ls -l
chmod +a ping.sh 
chmod a+x ping.sh 
ls -l
./ping.sh 
ls -l
more ping.sh 
./ping.sh 
more ping.sh 
./ping.sh 
ping 10.81.0.100
./ping.sh 
more ping.sh 
./ping.sh 
more ping.sh 
./ping.sh 
more ping.sh 
./ping.sh 
more ping.sh 
./ping.sh 
more ping.sh 
./ping.sh 
more ping.sh 
./ping.sh 
clear
./ping.sh 
clear
./ping.sh 
clear
./ping.sh 
sudo
su -
su -l
apt update
su -l
sudo apt udpate
useradd -aG sudo sstanev
su -
sudo apt update
su -l
sudo apt update
more .ssh/config
ssh -l admin 10.81.0.236
ssh -l admin@10.81.0.235
ssh -l admin 10.81.0.235
vi .ssh/config
sudo vi .ssh/config
ssh -l admin 10.81.0.235
sudo vi .ssh/config
ssh -l admin 10.81.0.235
ssh -l admin 10.81.0.234
cat .ssh/config 
sudo vi .ssh/config
ssh -l admin 10.81.0.234
ssh -l admin 10.60.0.236
sudo apt install software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt update
sudo vi /etc/apt/sources.list.d/ansible.list
sudo add-apt-repository --yes --update ppa:ansible/ansible
apt install software-properties-common
sudo apt install software-properties-common
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo vi /etc/apt/sources.list.d/ansible.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
sudo apt install gnupg
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
sudo apt update
sudo add-apt-repository --remove  ppa:ansible/ansible
apt update
sudo apt update
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
apt update
sudo apt update
sudo apt install ansible
ansible -v
ansible -V
ls -l
mkdir ansible
cd ansible/
mkdir gather_facts
cd gather_facts/
vi inventory
vi gather_fact.yml
ansible-playbook -i inventory gather_fact.yml 
vi gather_fact.yml 
cp gather_fact.yml gather_fact_v1.yml 
vi gather_fact_v1.yml 
vi inventory 
ansible-playbook -i inventory gather_fact.yml 
ansible-playbook -i inventory gather_fact.yml -vvvv
vi inventory 
ansible-playbook -i inventory gather_fact.yml
ansible-playbook -i inventory gather_fact_v1.yml
ls -l
ansible-playbook -i inventory gather_fact_v1.yml
vi gather_fact_v1.yml 
vi inventory 
ansible-playbook -i inventory gather_fact_v1.yml
ansible-playbook -i inventory gather_fact.yml
echo $output
more gather_fact.yml 
output
ansible-playbook -i inventory gather_fact_v1.yml
ansible-playbook -i inventory gather_fact_v1.yml -vvvv
vi inventory 
ansible-playbook -i inventory gather_fact_v1.yml
vi gather_fact_v1.yml 
ansible-playbook -i inventory gather_fact_v1.yml
cat gather_fact*
cat gather_fact_v1.yml 
cat gather_fact.yml 
ansible-playbook -i inventory gather_fact_v1.yml -v
code gather_fact.yml 
pwd
ls inventory 
more inventory 
ls -l
more gather_fact.yml 
more gather_fact_v1.yml 
ansible-playbook -i inventory gather_fact_v1.yml -v
ansible-playbook -i inventory gather_fact.yml -v
more  gather_fact.yml 
ansible-playbook -i inventory gather_fact.yml -v
ansible-playbook -i inventory gather_fact.yml -vv
reset
ansible-playbook -i inventory gather_fact.yml -vv
ansible-playbook -i inventory gather_fact.yml 
ls -l
rm gather_fact.yml 
rm gather_fact_v1.yml 
ansible-playbook -i inventory gather_facts_via_cmd.yml 
ansible-playbook -i inventory gather_fact_ios_facts.yml 
ls -l
ansible-playbook -i inventory gather_facts_specific_key.yml.yml 
ansible-playbook -i inventory gather_facts_specific_key.yml
ls -l
rm gather_fact_ios
ls -l
ansible-playbook -i inventory gather_facts_via_cmd.yml 
reset
ansible-playbook -i inventory gather_facts_via_cmd.yml 
ls -l
mkdir outputs
ansible-playbook -i inventory gather_facts_via_cmd.yml 
ls -l
more outputs/10.81.0.234.txt 
tree
tree ~/ansible/gather_facts/
sudo apt install tree
tree ~/ansible/gather_facts/
tree ~/ansible/
ls -l
ansible-playbook -i inventory gather_facts_generate_report.yml 
ls -l
ls -l outputs/
ansible-playbook -i inventory gather_facts_generate_report.yml 
more outputs/table_10.81.0.234.txt 
ansible-playbook -i inventory gather_facts_generate_report.yml 
more outputs/table_10.81.0.234.txt 
rm outputs/table_10.81.0.234.txt 
ansible-playbook -i inventory gather_facts_generate_report.yml 
rm outputs/table_10.81.0.234.txt 
ls -l outputs/table_10.81.0.234.txt 
ls -l outputs/
ansible-playbook -i inventory gather_facts_generate_report.yml 
ls -l outputs/table_10.81.0.234.txt 
more outputs/table_10.81.0.234.txt 
ls -la
tree
v outputs/str_json.py outputs/str_to_json.py 
mv outputs/str_json.py outputs/str_to_json.py 
tree
ansible-doc 
ansible
ansible-config 
ansible-doc 
ansible-doc -h
ansible -h
ansible-doc ios_facts
ls -l
ls -l Ansible/
rm -R Ansible/
ls -l
rm outputs/
rm -r outputs/
ls -l
rm g*
ls -l
rm inventory 
ls -l
cd Ansible/
ls -l
cd ..
ls -l
mv Ansible/ Ansible-Play1
ls -l
ls -l Ansible-Play1/outputs/
cd Ansible-Play1/
ansible-playbook -i inventory gather_facts_generate_report.yml 
more outputs/table_10.81.0.234.txt 
exit
ssh-keygen -t ed25519 -C "ansible key" 
ls -l
ls -la
ls -la .ssh/
exit
ls -la
ls -la .ssh/
ls -la .ssh/config 
cat .ssh/config 
ls -la .ssh/config 
ls -la .ssh/
ls -la .ssh/authorized_keys 
cat .ssh/authorized_keys 
exit
ls -l
cd ansible/
pwd
ls -l
cd gather_facts/
cd ..
mv ansible ansible_backup
ls -l
pwd
ls -l
cd  gather_facts/
ls -l
ansible-playbook -i inventory gather_facts_generate_report.yml 
ssh -l admin 10.81.0.234
ssh -l admin 10.81.0.235
ssh -l admin 10.60.0.236
ssh -l admin 10.81.0.234
ssh-keygen -f "/home/sstanev/.ssh/known_hosts" -R "10.81.0.234"
sudo ssh-keygen -f "/home/sstanev/.ssh/known_hosts" -R "10.81.0.234"
ssh -l admin 10.81.0.234
ansible-playbook -i inventory gather_facts_generate_report.yml 
ls 
cd ..
ls l
ls
cat github-info 
exit
ls -la
ls -l
ls -l gather_facts/
ls -l
