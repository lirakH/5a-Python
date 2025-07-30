1.Credentials 
Credentials are the pieces of information used to verify a user's identity. Common credentials include: 
  ● Username: A unique identifier for the user. 
  ● Password: A secret key known only to the user and the system. 

2. Authentication Methods 
Various methods can be used to authenticate users, each with its own advantages and use cases: 
  ● Password-Based Authentication: The most common form, where users provide a username and password. The server verifies these against stored credentials. 
  ● Multi-Factor Authentication (MFA): Enhances security by requiring two or more verification methods, such as a password and a mobile phone verification code. 
  ● Biometric Authentication: Uses physical characteristics like fingerprints or facial recognition for verification. 
  ● Token-Based Authentication: Involves the use of tokens (e.g., JWT) that are generated upon login and used for subsequent requests to verify identity. 

3. Authentication Protocols 
Protocols define how authentication data is transmitted and verified. Common protocols include: 
  ● OAuth2: A widely used authorization framework that allows third-party services to exchange authentication and authorization information. 
  ● SAML (Security Assertion Markup Language): Often used for single sign-on (SSO) in enterprise environments. 
  ● OpenID Connect: An identity layer on top of OAuth2, used for verifying user identities. 

To ensure robust security, follow these best practices: 
  ● Secure Password Storage: Use strong hashing algorithms like bcrypt to store passwords securely. 
  ● Use HTTPS: Encrypt data transmitted between the client and server to prevent interception. 
  ● Implement MFA: Add an extra layer of security by requiring multiple forms of verification. 
  ● Regularly Update Security Measures: Stay updated with the latest security practices to protect against evolving threats. 

4. Key Concepts in Authorization:
  ● Roles and Permissions: 
    ● Roles: Roles are predefined sets of permissions. For example, a user might have a role of "admin," "editor," or "viewer." Each role is associated with a specific set of permissions. 
    ● Permissions: Permissions are specific actions that a user can perform. For example, permissions might include "read," "write," "delete," or "execute" on a particular resource. 
  ● Access Control: 
    ● Access Control Lists (ACLs): ACLs are lists that define which users or system processes have access to objects and what operations they can perform on those objects. 
    ● Role-Based Access Control (RBAC): RBAC assigns permissions to roles rather than to individual users. Users are then assigned roles, simplifying the management of permissions. 
    ● Attribute-Based Access Control (ABAC): ABAC uses attributes (user attributes, resource attributes, environment attributes) to determine access permissions. 
  ● Policies: 
    ● Policies are rules that govern the authorization process. These rules define the conditions under which access is granted or denied. Policies can be based on user roles, time of access, location, and other factors. 

5. How Authorization Works 
  ● User Authentication: The user first logs in to the system using their credentials. This process confirms their identity. 
  ● Token Issuance: Upon successful authentication, the system issues a token (e.g., JWT) containing the user's identity and possibly their roles or permissions. 
  ● Access Request: When the user attempts to access a resource or perform an action, they include the token in their request. 
  ● Token Validation: The system validates the token to ensure it is authentic and has not expired. 
  ● Authorization Check: The system checks the user's roles or permissions against the access control policies to determine if the requested action is allowed. 
  ● Access Granted or Denied: Based on the authorization check, the system either grants or denies access to the resource.

Requirments:
  - fastapi
  - uvicorn
  - pydantic
  - python-dotenv
