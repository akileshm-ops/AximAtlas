# Project-Scoped Rules

## Dependency Management Rule
Before writing code that imports from a third-party library, **always verify that the library is installed** in `package.json`. If it is not installed, run the installation command (e.g., `npm install <package>`) *before* or *immediately after* writing the code, and ensure it finishes successfully to avoid runtime `Module not found` or `ReferenceError` crashes. 

Never assume a sub-package (like `@react-three/drei`) is installed just because the parent package (`@react-three/fiber`) is.
