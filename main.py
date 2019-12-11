from models import Base


def main():
    Base.metadata.create_all()



if __name__ == '__main__':
    main()
