from auth import login_user
 
def main():
    print("Starting login...")
    login_user("admin", "password")
 
if __name__ == "__main__":
    main()