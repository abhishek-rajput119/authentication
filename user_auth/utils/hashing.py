import bcrypt
import secrets


class PasswordHasher:
    def generate_salt(self):
        """
        Generate a random salt.

        Returns:
        - A randomly generated salt.
        """
        return bcrypt.gensalt()

    @staticmethod
    def hash_password(password, salt):
        """
        Hash the given password using the provided salt.

        Parameters:
        - password: The password to be hashed.
        - salt: The salt used for hashing.

        Returns:
        - The hashed password.
        """
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def hash_password_with_new_salt(self, password):
        """
        Generate a new salt, hash the given password, and return the salt and hashed password.

        Parameters:
        - password: The password to be hashed.

        Returns:
        - A tuple containing the salt and hashed password.
        """
        salt = self.generate_salt()
        hashed_password = self.hash_password(password, salt)
        return salt, hashed_password
