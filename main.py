from honeypot.ssh_service import start_ssh_honeypot
from deception.polymorphic_engine import start_profile_rotation


def main():
    print("Starting Poly-Honey IoT Honeypot System...")

    # Start polymorphic identity rotation
    start_profile_rotation()

    # Start SSH honeypot service
    start_ssh_honeypot()


if __name__ == "__main__":
    main()