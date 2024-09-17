# images-development

A collection of Docker images for development with main programming languages.

They can be used alone but are designed to work with the [Onyxia](https://github.com/InseeFrLab/onyxia) ecosystem.

## Layouts

```mermaid
  graph LR;
      B[base]:::base-->JAVA_MINIMAL[java-minimal]:::minimal;
      JAVA_MINIMAL-->JAVA_MAVEN[java-maven]:::package;
      JAVA_MAVEN--> VSCODE_MAVEN[java-maven-vscode]:::ide;
      classDef base fill:#d2f9ff,color:#000  ;
      classDef minimal fill:#C1D5DF,color:#000;
      classDef package fill:#3cb5f2 ,color:#000  ;
      classDef ide fill:#0072d9  ;
```