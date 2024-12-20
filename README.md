# Social Network System

This repository implements a **Social Network System** designed to simulate core features of modern social networks, such as user interactions, posts, likes, comments, and notifications. The system demonstrates the use of object-oriented principles and design patterns to create a robust, scalable, and maintainable framework.

## Features
- **User Management**: Users can sign up, log in, log out, and manage their social connections (follow/unfollow other users).
- **Post Management**: Users can create different types of posts, including text, image, and sale posts.
- **Interaction**: Users can like and comment on posts, receive notifications, and interact with other users' content.
- **Dynamic Notifications**: Notifications are triggered for likes, comments, and other interactions.
- **Sales Management**: Sale posts include pricing, discounts, and the ability to mark products as sold.

## Design Patterns Used

### 1. **Observer**
- **Purpose**: Enables users to receive dynamic notifications about interactions (likes, comments, etc.) on their posts or activities in their network.
- **Example**:
    - Users automatically receive updates when someone likes or comments on their posts.
    - Notifications are stored for each user for later retrieval.
- **Advantages**:
  - Decouples the notification mechanism from user and post management.
  - Simplifies the addition of new notification types.

### 2. **Strategy**
- **Purpose**: Allows for dynamic behavior customization, such as applying discounts to sale posts.
- **Example**:
    - Sale posts use a discount strategy to adjust prices dynamically based on user input.
- **Advantages**:
  - Enables flexibility in implementing various discount strategies or pricing policies without modifying the core post functionality.

## Code Structure

- **`SocialNetwork`**:
  - Manages the core functionality of the network, including user management, login/logout, and overall system operations.

- **`User`**:
  - Represents individual users, allowing them to follow/unfollow others, create posts, and interact with content.

- **`Post`**:
  - A base class for all types of posts (text, image, sale).
  - Includes interaction features such as liking and commenting.

- **Notification System**:
  - Uses the Observer pattern to manage user notifications for interactions on posts.

## Example Usage

### Setting Up the Network:
```python
from SocialNetwork import SocialNetwork

# Initialize the social network
network = SocialNetwork("Twitter")

# Create users
u1 = network.sign_up("Alice", "pass1")
u2 = network.sign_up("Bob", "pass2")
```

### Managing Followers:
```python
# Users follow each other
u1.follow(u2)
u2.follow(u1)
```

### Creating Posts:
```python
# User creates a text post
p1 = u1.publish_post("Text", "Exploring the world of social networks!")
# User creates an image post
p2 = u2.publish_post("Image", "beautiful_photo.jpg")
```

### Interacting with Posts:
```python
# Users like and comment on posts
p1.like(u2)
p2.comment(u1, "Amazing picture!")
```

### Notifications:
```python
# View notifications for a user
u1.print_notifications()
```

## Running the System

1. Clone the repository:
   ```bash
   git clone https://github.com/AmitGini/SocialNetworkAssignment.git
   cd SocialNetworkAssignment
   ```

2. Run the main script:
   ```bash
   python main.py
   ```

3. Interact through the terminal to explore user activities, posts, and notifications.

## Example Output

The system simulates user interactions, demonstrating how posts are created, interactions are managed, and notifications are handled. Example console outputs:
- User `Alice` follows `Bob`.
- `Alice` creates a text post, and `Bob` likes it.
- Notifications appear dynamically for actions taken on posts.

## Acknowledgments

This project illustrates the use of object-oriented principles and design patterns in developing a feature-rich social network simulation. It serves as an example of implementing modular and maintainable software systems.

## Contributing

Contributions are welcome! Feel free to fork the repository, submit pull requests, or open issues for enhancements or bug fixes.

## License

[MIT](https://choosealicense.com/licenses/mit/)
