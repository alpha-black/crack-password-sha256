import hashlib

cracked = 0;
passPrefix = '';
salt = '';
userName = '';
out = open ('results', 'w');

def computeAndCheck (word):
  h = hashlib.new ('sha256');
  guess = passPrefix  + word + salt;
  h.update (guess);
  guessHash = h.hexdigest();
  guessHash = guessHash[:32];
  if guessHash == passHash:
    out.write ('Cracked - ' + word);
    cracked = 1;
  return;

#Try username combinations
def userNameGuess (pattern):
  for p in pattern:
    guess1 = userName;
    guess2 = p + userName;
    guess3 = userName + p;
    computeAndCheck(guess1);
    if cracked == 1:
      break;
    computeAndCheck(guess2);
    if cracked == 1:
      break;
    computeAndCheck(guess3);
    if cracked == 1:
      break;
  return;

#Wordlist
def wordListGuess(f):
  for word in f:
    word = word[:-1];
    computeAndCheck (word);
    if cracked == 1:
      break;
  return;

#f = open ('/usr/share/dict/words', 'r');
f = open ('wordlist_crackstation.txt', 'r');
pattern = open ('guess.txt', 'r');

passPrefix = 'potplantpwdb';
userName = raw_input ('Enter username: ');
salt = raw_input ('Enter salt: ');
passHash = raw_input ('Enter passwor Hash: ');
userNameGuess (pattern);
if cracked == 0:
  wordListGuess (f);
