import random

cities = ['Bath', 'Birmingham', 'Bradford', 'Brighton', 'Bristol', 'Cambridge', 'Canterbury', 'Cardiff', 'Carlisle',
          'Chelmsford', 'Chester', 'Chicester', 'Coventry', 'Derby', 'Durham', 'Ely', 'Exeter', 'Gloucester', 'Hereford',
          'Kingston upon Hull', 'Lancaster', 'Leeds', 'Leicester', 'Lichfield', 'Lincoln', 'Liverpool', 'London',
          'Manchester', 'Newcastle', 'Norwich', 'Nottingham', 'Oxford', 'Peterborough', 'Plymouth', 'Portsmouth',
          'Preston', 'Ripon', 'St Albans', 'Salford', 'Salisbury', 'Sheffield', 'Southampton', 'Stoke-on-Trent',
          'Sunderland', 'Truro', 'Wakefield', 'Wells', 'Winchester', 'Wolverhampton', 'Worcester', 'York']

regions = ['the North', 'the North-East', 'the North-West', 'the East', 'the Midlands', 'the South-West',
           'the South-East', 'the West', 'the South']

counties = ['Bath and North East Somerset', 'Bedfordshire', 'Berkshire', 'Bristol', 'Buckinghamshire', 'Cambridgeshire',
            'Cheshire', 'Cornwall', 'County Durham', 'Cumbria', 'Derbyshire', 'Devon', 'East Riding of Yorkshire',
            'East Sussex', 'Essex','Gloucestershire', 'Greater London', 'Greater Manchester', 'Hampshire',
            'Herefordshire', 'Hertfordshire', 'Isle of Wight', 'Isles of Scilly', 'Kent', 'Lancashire', 'Leicestershire',
            'Lincolnshire', 'Merseyside', 'Norfolk', 'North Somerset', 'North Yorkshire', 'Northamptonshire',
            'Northumberland', 'Nottinghamshire', 'Oxfordshire', 'Rutland', 'Shropshire', 'Somerset',
            'South Gloucestershire', 'South Yorkshire', 'Staffordshire', 'Suffolk', 'Surrey', 'Tyne & Wear',
            'Warwickshire', 'West Midlands', 'West Sussex', 'West Yorkshire', 'Wiltshire', 'Worcestershire']



extra_professions = ['Tenants', 'Landlords', 'Doctors', 'Nurses', 'Teachers', 'Bankers', 'Parents',
               'Actors', 'Musicians', 'Athletes', 'Housewives', 'Consultants', 'Lawyers', 'Technicians', 'Project Managers',
               'Engineers', 'Gardeners', 'Plumbers', 'Carpenters', 'Builders', 'Investors', 'Drivers', 'Tree Surgeons',
               'Administrators', 'Civil Servants', 'CEOs', 'Surveyors', 'Vets', 'Chefs', 'Scientists', 'Artists', 'Hairdressers',
               'Accountants', 'Psychologists', 'Therapists', 'Dentists', 'Secretaries', 'Firefighters', 'Software Developers',
               'Actuaries', 'Designers', 'Mechanics', 'Cleaners', 'Cashiers', 'Librarians', 'Tailors', 'Bakers', 'Candlestick Makers',
               'Opticians', 'Pilots', 'Bartenders']

constraint = ["can't", "can only", "must", "must not"]

action = ["take the train", "go to the shops", "drive to lidl", "watch football", "exercise", "eat", "drink",
          "read", "go on holiday", "quarantine", "meet people", "sing", "perform magic", "train as emergency nurses",
          "walk in circles", "order takeaway", "socialise", "pay taxes", "talk to their neighbours", "research a vaccine",
          "go to work", "hire a van", "learn French", "speak Italian", "cook sausages", "trade fruit", "host a farmers market",
          "learn the trumpet", "investigate what happened to flight MH370", "compost", "take the bins out", "heckle a bus driver",
          "commute by bicycle", "run everywhere", "hoard loo roll", "take vitamin C", "drink milk", "lift weights", "go to Church",
          "learn the St Crispin's Day speech from Henry V", "avoid weasels", "leave their houses", "enter their houses",
          "stare at the sun", "have their hair cut", "ride a horse", "contemplate the meaning of life", "leave an Amazon review",
          "use their wing-mirrors", "speak", "shout", "dig a hole", "purchase fire-wood", "remember their friends", "fox hunt",
          "sing karaoke", "go to the gym", "explore caligraphy"]

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

time_of_day = ['in the morning', 'in the afternoon', 'in the evening', 'at night']

hours = [1,2,3,4,5,6,7,8,9,10,11,12]

T_F = [True, False]

if_conditions = ['are over 6ft tall', 'weigh less than 6 stone', 'have had their wisdom teeth removed',
                 'will consider giving blood', 'have ever been sunburnt', 'know where the treasure is buried',
                 'are older than 40', 'are younger than 25', 'collect coupons', 'own a microwave', 'take steroids',
                 'have blue eyes', 'have had a hair transplant', 'take iron supplements', 'have a BMI of more than 40',
                 'have a driving license', 'have a personal best of more than 6 metres in the long jump',
                 'are allergic to shellfish', "have approval", "are not superstitious", 'have a broken leg',
                 'have 20/20 vision', 'are forgetful', "don't want to", "have seen a senior member of government doing it",
                 "are unhappy", "had to cancel a wedding", 'have been to Canterbury', 'train really hard', 'know what their VO2 max is',
                 'are pregnant', 'are allergic to penicillin', 'have really bad hayfever', 'are ambidextrous',
                 'are able to complete a Rubix cube in under 10 seconds', 'are a bit funny looking', 'are Welsh',
                 'are lazy', 'are wearing a mask under their chin', "unable to remember their parents' birthdays",
                 'are undisputed heavyweight champion on the world', 'are financially irresponsible']

def generate_rule(act_set):
    limit = random.choice(constraint)
    act = random.choice(action)
    if len(act_set) == 0:
        pass
    elif act in act_set:
        while act in act_set:
            act = random.choice(action)
    act_set.append(act)
    day_crit = random.choice(T_F)
    some_time = random.choice(T_F)
    rand_bool = random.choice(T_F)
    include_if = random.randrange(1,10)
    labels_for_people = random.choice([extra_professions, 'People', 'People'])
    if labels_for_people != 'People':
        people = random.choice(extra_professions)
    else:
        people = labels_for_people
    str = f"{people} {limit} {act}"
    if day_crit:
        day = random.choice(days)
        str += f" on {day}"
    if some_time:
        if rand_bool:
            time = random.choice(time_of_day)
            str += f" {time}"
        else:
            time_1 = random.choice(hours)
            time_2 = random.choice(hours)
            str += f" between {time_1} and {time_2}"
    if include_if > 8:
        condition = random.choice(if_conditions)
        str += f" if they {condition}"
    return str, act_set


def get_places(places_set):
    place_num = random.randrange(1, 6)
    place_list = []
    for i in range(place_num):
        place = random.choice([cities, regions, counties])
        attach = random.choice(place)
        if len(places_set) == 0:
            pass
        elif attach in places_set:
            while attach in places_set:
                place = random.choice([cities, regions, counties])
                attach = random.choice(place)
        place_list.append(attach)
        places_set.append(attach)
    return place_list, places_set


def generate_tiers():
    tiers = random.randrange(1,5)
    places_set = ['Start']
    act_set = ['Start']
    if tiers is 1:
        state = "National Lockdown"
        rules = []
        rule_num = random.randrange(8, 10)
        for x in range(rule_num):
            tmp_rule, act_set = generate_rule(act_set)
            rules.append(tmp_rule)
        return state, rules
    else:
        state = "Tiered Restrictions"
        out = []
        for i in range(1, tiers+1):
            rule_num = random.randrange(4, 6)
            tier = dict()
            tier['lvl'] = i
            rules = []
            for x in range(rule_num):
                tmp_rule, act_set = generate_rule(act_set)
                rules.append(tmp_rule)
            tier['rules'] = rules
            tier['places'], places_set = get_places(places_set)
            out.append(tier)
        return state, out

