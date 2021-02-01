tf = [
    {'th_name': '朱伟', 't_id': 1, 'c_id': 4, 'class_name': '初中二年级'},
    {'th_name': '朱伟', 't_id': 1, 'c_id': 5, 'class_name': '小学一年级'},
    {'th_name': '汤家凤', 't_id': 2, 'c_id': 8, 'class_name': '初中一年级'},
    {'th_name': '张宇', 't_id': 3, 'c_id': 6, 'class_name': '小学五年级'},
    {'th_name': '张宇', 't_id': 3, 'c_id': 10, 'class_name': '初中三年级'},
    {'th_name': '张宇', 't_id': 3, 'c_id': 8, 'class_name': '初中一年级'},
    {'th_name': '武忠祥', 't_id': 4, 'c_id': 6, 'class_name': '小学五年级'}
]

tn = {}

for row in tf:
    tid = row['t_id']
    if tid in tn:
        tn[tid]['c_name'].append(row['class_name'])
    else:
        tn[tid] = {'tid': row['t_id'], 'th_name': row['th_name'],'c_name': [row['class_name'], ]}

    print(tn)
