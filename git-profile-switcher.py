import subprocess

def main() :
  command, profiles = "", {
    "a": ["Intcrzyppl", "griffith@intcrzyppl.com"],
    "b": ["PirpleLabs", "griffith@pirplelabs.com"],
    "c": ["Personal [dolphtech]", "griffith@dolphtech.com"]
  }

  print("Welcome to git profile switcher.")
  print("""
    a ==> Intelligent Crazy People
    b ==> Pirplelabs
    c ==> Personal Github
  """)

  try:
    option = input('Enter your option :> ')
    command = "git config --global user.email '{}'".format(profiles[option][1])
    subprocess.call(command.split(" "), shell=False)
    result = subprocess.check_output('git config --global user.email'.split(" "))
    print('You changed the profile {} - {}'.format(profiles[option][0], profiles[option][1]))
  
  except Exception as e:
    print('An error occured. {}'.format(str(e)))

if __name__ == "__main__":
    main()