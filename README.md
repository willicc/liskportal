# LISK PORTAL 

![banner](image.png)

**The L2 for Real World Solutions in Emerging Markets**
Lisk Portal is the gateway to the Lisk ecosystem, providing access to a cost-efficient and scalable L2 network secured by Ethereum and part of the OP Superchain.

## Description

- Register here : https://portal.lisk.com/airdrop
- Register with wallet and follow instructions there
- Submit Code
  ```
  OUrd4I
  ```
  
- Deposit to LISK MAINNET, just not too much to paying gas fee
- Bridge here: https://superbridge.app/lisk-mainnet
- The Script will do 75 onchain tx each day so we can get max points each week [500 points].


## Instalation
```bash
git clone https://github.com/Zlkcyber/liskportal.git
cd liskportal
```
install the packages
```bash
pip install -r requirements.txt
```
**Edit pvkey.txt and input Private Key**
```bash
nano pvkeys.txt
```
run the script
```bash
python3 main.py
```

## Optinally you can use pm2 to run script in the background
You can use pm2 to run your script in the background, allowing it to continue running even after you close your terminal.

### Installing pm2

If you haven't installed pm2, you can do so globally with npm:
```bash
npm install -g pm2
```
### Start the Script
```bash
pm2 start main.py --name liskportal
```

## Managing pm2 Processes
You can manage your pm2 processes with the following commands:
- List running processes:
```bash
pm2 list
```
- Restart a process:
```bash
pm2 restart liskportal
```
- Stop a process:
```bash
pm2 stop liskportal
```
- View logs:
```bash
pm2 logs liskportal
```


## ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the [MIT License](LICENSE).