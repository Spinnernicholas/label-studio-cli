import argparse
import label_studio

def manage_users(subparsers):
    user_parser = subparsers.add_parser('user', help='Manage users.')
    user_parser.add_argument('action', choices=['add', 'remove', 'list'], help='The action to perform.')
    user_parser.add_argument('--username', help='The username of the user.')

def manage_projects(subparsers):
    project_parser = subparsers.add_parser('project', help='Manage projects.')
    project_parser.add_argument('action', choices=['add', 'remove', 'list'], help='The action to perform.')
    project_parser.add_argument('--name', help='The name of the project.')

def main():
    parser = argparse.ArgumentParser(description='CLI for managing Label Studio.')
    subparsers = parser.add_subparsers(title='Commands', dest='command')

    manage_users(subparsers)
    manage_projects(subparsers)

    args = parser.parse_args()

    if args.command == 'user':
        if args.action == 'add':
            print(f'Adding user {args.username}...')
            # Add user logic here
        elif args.action == 'remove':
            print(f'Removing user {args.username}...')
            # Remove user logic here
        elif args.action == 'list':
            print('Listing users...')
            # List users logic here

    elif args.command == 'project':
        if args.action == 'add':
            print(f'Adding project {args.name}...')
            # Add project logic here
        elif args.action == 'remove':
            print(f'Removing project {args.name}...')
            # Remove project logic here
        elif args.action == 'list':
            print('Listing projects...')
            # List projects logic here

if __name__ == '__main__':
    main()