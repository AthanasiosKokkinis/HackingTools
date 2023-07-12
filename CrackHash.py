import hashlib # To hash passwords and compare with original
import threading # Fake threading
import glob # Take all txts

def getAllWordlistPaths(wordlist_folder):
    path_pattern =  wordlist_folder + "\*.txt"
    file_paths = glob.glob(path_pattern)
    return file_paths


def crackHashWithWordlists(target_hash, hash_alg, wordlists, output = None):
    hash_alg = hash_alg.lower()
    if hash_alg not in hashlib.algorithms_guaranteed:
        print("Hash algorithm selected doesn't exist")
        exit(-1)
    hash_alg = getattr(hashlib, hash_alg)
    for wordlist in wordlists:
        password_file = open(wordlist,"r")
        for password in password_file:
            pass_hash = hash_alg(password.encode("utf-8").strip()).hexdigest()
            print(pass_hash)
            if target_hash == pass_hash:
                print("Password = " + password)
                if output != None:
                    file = open(output,"a")
                    file.write("Password = " + password)
                    file.close()
    
def splitWordlistsToThreads(wordlists, num_threads):
    k, m = divmod(len(wordlists), num_threads)
    a = wordlists
    return list((a[i*k+min(i, m):(i+1)*k+min(i+1,m)] for i in range(num_threads)))

def main(target_hash, wordlist_folder, num_threads, hash_alg = "md5", output = None):
    txt_paths = getAllWordlistPaths(wordlist_folder)
    wordlist_each_thread = splitWordlistsToThreads(txt_paths, 2)
    for wordlist in wordlist_each_thread:
        thread = threading.Thread(target = crackHashWithWordlists, args = [target_hash, hash_alg, wordlist, output])
        thread.start()
    
hash_to_crack = ""
folder_to_wordlists = ""
threads =
output_folder = r""
hashlib_alg = ""
main(hash_to_crack, folder_to_wordlists, threads, hashlib_alg, output_folder)

