# Plivo CallCentre Offering(PCO)

## Getting Started

```
git clone https://github.com/deepakplv/pco.git
virtualenv -p python3.6 env
source env/bin/activate
pip install pinax-cli
cd call_centre
npm install
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata sites
npm run dev
```

Browse to http://localhost:3000/
