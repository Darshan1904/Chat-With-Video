# Smart Stream - Engage Smarter, Not Longer

## Gemini API Developer Competition

### The Team
- Darshan Patel
- Divy Awasthi
- Swayam Desai
- Ved Chadderwala

## Introduction
As a user, consuming and engaging with video content is very important in this fast-moving digital world today. Utilizing the Gemini API, we have developed an innovative and user-engaging application that allows users to watch YouTube videos without going through the entire length of the video. This will help in not only best content interaction but also saving time which is far precious.

## Background
The consumption of video content is at an all-time high, and users are struggling to keep up with the information overload. Our app reaches a middle ground where we represent video data in terms of simple reading so anyone can quickly get an overview. The screens, in this framework, work with the will of users who want to understand more quickly what a video is about and interact better than your content.

## Implementation
1. **Obtaining the transcript from the video link**  
   We utilize the Assembly API to get transcripts for YouTube videos. This is the step of our process where the raw video content transformed into text file - readable form for further analysis.
2. **Summarizing the transcript**  
   And then using the Gemini API to create summaries of it. This breaks the content down to its essence, so users can grasp what matters without watching a whole video.
3. **Interactive Platform**  
   The content of each paper is then summarized and displayed in a user-friendly interface created using Streamlit. Users interact via a chat using the Gemini API to query information regarding the content of videos. This interaction occurs in real time, improving the user experience and making it more accessible.

## Tech Stack
- **Frontend:** Streamlit, supporting chat backup history
- **Authentication and Storage:** Firebase
- **Summarizing and Chatting:** Gemini API
- **Transcripts:** Groq API, Assembly API

This documentation outlines the framework and functionalities of our application, which is designed to streamline the way users interact with video content, making it an efficient and time-saving tool in the digital media landscape.

## Flutter Application Extension

In addition to the web-based platform, we've extended these features into a Flutter application, bringing the same powerful capabilities to mobile users. The Flutter app provides a seamless user experience with Firebase authentication, ensuring secure and personalized access. Users can log in, browse summarized video content, and interact with the app just as they would on the web version, making Smart Stream a versatile tool for efficient video consumption across platforms.

This documentation outlines the framework and functionalities of our application, designed to streamline video content interaction, making it an efficient and time-saving tool in today's digital media landscape.
