# onboarding-checklist-generator

Generate a new-starter onboarding checklist from a JSON role template (common items plus role-specific items).

## How to run

```sh
python3 main.py template.json --name "Ayesha Khan" --role "IT Support"
```

## Example output

```
Onboarding checklist for Ayesha Khan (IT Support):
[ ] 1. Create account
[ ] 2. Issue laptop
```

Standard library only. Run the tests with `python3 -m unittest discover`.
