<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#changelog">Changelog</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About the Project

<div style="text-align: center;">
  <img src="https://user-images.githubusercontent.com/108723117/206897790-f8fc0719-3f5c-402d-824d-1aeeb979d2cd.png" width="500" height="700"/>
</div>

The goal of the **Weconnect CIT** project is to develop and implement a simple user application and a corresponding web-based administration tool for Volunteering Victoria and its associated parties. The user application will empower volunteers associated with Volunteering Victoria to participate in surveys, while the web app will provide administrators with valuable insights and statistics derived from these surveys. By building these components, we aim to facilitate efficient data collection, analysis, and decision-making to enhance the impact of volunteering efforts.

*Key Features of the Volunteer Tool:*
- Receive an email with a temporary password upon volunteer registration.
- Be able to securely update and change a users password.
- Take surveys to reflect on progress.
- Automatically receive mobile notifications to complete pending surveys to be completed (IN PROGRESS).

*Key Features of the Administration Tool:*
- View aggregate changes in survey results for an organisation.
- Slice data by theme, date, and specific questions.
- Register new volunteers to an organisation and Volunteering Victoria.

### Built With

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![Org Mode](https://img.shields.io/badge/pygame-%2377AA99.svg?style=for-the-badge&logo=org&logoColor=white)
* ![Deepin](https://img.shields.io/badge/pyinstaller-007CFF?style=for-the-badge&logo=deepin&logoColor=white)

<p align="right">(<a href="#about-the-project">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

To run this project you will need to have npm and node installed as core dependencies.

#### Using a Node Installer
Using a Node installer to install Node.js and npm
If you are unable to use a Node version manager, you can use a Node installer to install both Node.js and npm on your system.

[npm-installer]

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/lezhou8/it-project-team-34.git
   ```
2. Install NPM packages in all directories including inside the back_end, front_end_mobile_app and front_end folders.
   ```sh
   npm install
   ```
3. Replace the contents of the .env by following the set up instructions for MongoDB in /docs

<p align="right">(<a href="#about-the-project">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To start up all aspects of this software, run
```{sh}
npm run start
```

### Front End Administration Tool
To start up the front end react app, run
```{sh}
npm run front-admin
```

### Front End Volunteer Tool
To start up the front end react app, run
```{sh}
npm run front-user
```

### Back End
To start up the front end react app, run
```{sh}
npm run back
```

<p align="right">(<a href="#about-the-project">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [X] Implement Static Version of the Administration tool
- [X] Implement Static Version of the Volunteer tool
- [X] Write the API Calls for our Apps
- [X] Modify Static Versions of our Apps to leverage our API
- [X] Create Documentation for our API
- [ ] Add Documentation in a /docs Folder
- [ ] Add Test cases in a /test Folder


<p align="right">(<a href="#about-the-project">back to top</a>)</p>

<!-- ROADMAP -->
## Changelog
#### V1.0
**Date - August 9th, 2023 - August 27th, 2023**

#### V2.0
**Date - September 1st, 2023 - September 20th, 2023**

- US3.1_FRONT Volunteers can login and logout of the app
- US5.2_FRONT Organisation admins can log in (securely)
- US5.3_FRONT Organisation admins can log in (securely)
- US2.1_FRONT Volunteers can take surveys
- US2.2_FRONT Volunteers can skip questions
- US7.1_BACK Admins can view aggregate changes in results
- US7.3_FRONT Admins can slice data by theme, date and specific question
- US8.1_BACK VV Admins can log in (securely)
- US8.2_BACK VV Admins can log out (securely)

#### V3.0
**Date - September 20th, 2023 - October 18th, 2023**

- US1.1_ALL Volunteers receive an email with a temporary password upon registration
- US3.1_ALL Volunteers can login and logout of the app
- US5.2_ALL Organisation admins can log in (securely)
- US5.3_ALL Organisation admins can log in (securely)
- US6.2_ALL/US11.4_ALL Admins can register volunteers under their organisation
- US2.1_ALL Volunteers can take surveys
- US2.2_ALL Volunteers can skip questions
- US6.3_BACK Organisation admins can remove volunteers from their organisation
- US7.1_ALL/US10.1_ALL Admins can view aggregate changes in results
- US7.3_ALL/US10.2_ALL Admins can slice data by theme, date and specific question
- US8.1_ALL VV Admins can log in (securely)
- US8.2_ALL VV Admins can log out (securely)
- US9.2_BACK VV Admins can remove volunteers

<p align="right">(<a href="#about-the-project">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[npm-installer]: https://nodejs.org/en/download/
