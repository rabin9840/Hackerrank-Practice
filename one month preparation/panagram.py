def pangrams(s):
    # Write your code here
    return 'pangram' if len(set(s.replace(' ','').lower()))==26 else 'not pangram'