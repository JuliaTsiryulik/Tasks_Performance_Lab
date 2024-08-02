import json
import sys

def fill_values(test_structure, values_dict):
  for test in test_structure:

    test_value = values_dict.get(test['id'])
    if test_value:
      test['value'] = test_value
    
    if 'values' in test:
      fill_values(test['values'], values_dict)


def main(values_file, tests_file, report_file):

  with open(values_file, 'r', encoding='utf-8') as vf:
    values = json.load(vf)

  with open(tests_file, 'r', encoding='utf-8') as tf:
    tests = json.load(tf)

  values_dict = {item['id']: item['value'] for item in values['values']}

  fill_values(tests['tests'], values_dict)

  report = {'report': tests['tests']}

  with open(report_file,'w', encoding='utf-8') as rf:
    json.dump(report, rf, ensure_ascii=False, indent=4)

values_file = sys.argv[1]
tests_file = sys.argv[2]
report_file = sys.argv[3]

main(values_file, tests_file, report_file)
