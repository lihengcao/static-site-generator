python3 -m venv .venv
source .venv/bin/activate
printf "\nPackages Before:\n"
pip list
pip install -r static-site-generator/requirements.txt
printf "\nPackages After:\n"
pip list