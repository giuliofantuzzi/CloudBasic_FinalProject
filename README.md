# Cloud basic: Final Project
Final Project of the course *Cloud computing* (MSc DSAI, University of Trieste)

## Student's info

| Name | Surname | Student ID | UniTs email | Personal email | Course |
|:----:|:-------:|:----------:|:-----------:|:--------------:|:------:|
| Giulio | Fantuzzi | SM3800012 | GIULIO.FANTUZZI@studenti.units.it | giulio.fantuzzi01@gmail.com | DSAI|

## Project structure

```
📂 CloudBasic_FinalProject/
│
├── 📄 create_usr.sh
│ 
├── 📂 data/
│   └── ...files that will be created...
│
├── 📄 delete_usr.sh
│
├── 🐳 docker-compose.yml
│
├── 📄 generate_files.sh 
│
├── 📂 locust-tests/
│   └── 🐍 locustfile.py
│
├── 📰 README.md
│
└── 🏗️ setup.sh
```

## User instructions

I prepared some bash scripts in order to facilitate for you the whole testing process (so I won't do a lazy explanation of how to setup everything). The only requirement that I assume is that you are already equipped with Docker, bundled with Docker Compose.

The [`setup.sh`](setup.sh) script, as its name suggests, is meant to set up the working environment. More precisely, it will set the default storage quote-per-user, enable files encryption and set trusted domain. Since some users and files are required to perform the testing phase with Locust, the script will also create automatically 50 users and files of different dimensions (they will be saved into [data/](data/)).

**<u>Important note:</u>** for my project I decided to use 50 users. Since the user creation phase requires some minutes, you may be interested in reduce the number of users to test. In that case, remember to update also the python script [`locustfile.py`](locust-tests/locustfile.py) (line 13)!

In summary, the first step to perform is: 

```bash
docker-compose up -d
```

then launch the setup file with:

```bash
sh setup.sh
```

Once the `setup.sh` run is completed, you can perform tests on Locust simply going to [http://localhost:8080](http://localhost:8080)
