import 'package:chat_with_video/main.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:chat_with_video/values/colors.dart';
import 'package:chat_with_video/values/fonts.dart';

void main() {
  runApp(HomePageScreen());
}

class HomePageScreen extends StatelessWidget {
  const HomePageScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true, // Center the image in the AppBar
        title: SizedBox(
          height: kToolbarHeight, // Set the height to the height of the AppBar
          child: Image.asset(
            'assets/images/logobg.jpg',
            fit: BoxFit.contain, // Ensure the image fits within the available height
          ),
        ),
        backgroundColor: AppColors.newColor, // Make AppBar transparent
        elevation: 0, // Remove shadow
      ),
      body: HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final TextEditingController _urlController = TextEditingController();
  final TextEditingController _messageController = TextEditingController();
  final List<Map<String, String>> _chatMessages = [];
  String _summary = '';

  void _handleSubmitUrl() async {

    String url = _urlController.text;
    String apiUrl = 'http://10.0.2.2:5000/transcribe';

    debugPrint('Sending URL to API: $url');

    try {
      final response = await http.post(
        Uri.parse(apiUrl),
        headers: {
          'Content-Type': 'application/json',
        },
        body: json.encode({'videoURL': url}),
      );

      debugPrint('Response status code: ${response.statusCode}');

      if (response.statusCode == 200) {
        setState(() {
          _summary = jsonDecode(response.body)['summary'];
          debugPrint('Summary received: $_summary');
        });
      } else {
        debugPrint('Failed to get summary. Status code: ${response.statusCode}');
      }
    } catch (e) {
      debugPrint('Error occurred: $e');
    }
  }

  void _handleSendMessage() async {
    String message = _messageController.text;
    if (message.isEmpty) return;

    setState(() {
      _chatMessages.add({"role": "user", "message": message});
    });

    String response = await _getChatResponse(message);

    setState(() {
      _chatMessages.add({"role": "bot", "message": response});
    });

    _messageController.clear();
  }

  Future<String> _getChatResponse(String message) async {

    String apiUrl = 'http://10.0.2.2:5000/query';

    try {
      final response = await http.post(
        Uri.parse(apiUrl),
        headers: {
          'Content-Type': 'application/json',
        },
        body: json.encode({'query': message}),
      );

      // Log the status code of the response
      debugPrint('Response status code: ${response.statusCode}');

      if (response.statusCode == 200) {
        debugPrint('Response received');
        return jsonDecode(response.body)['result'];
      } else {
        debugPrint('Failed to get response. Status code: ${response.statusCode}');
        return "Chat Failed due to technical reasons.";
      }
    } catch (e) {
      debugPrint('Error occurred: $e');
      return '';
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [

          // Header - logo + tagline
          Container(
            alignment: Alignment.center,
            decoration: const BoxDecoration(
              color: AppColors.newColor,
              // color: AppColors.secondaryColor,
            ),
            height: MediaQuery.of(context).size.height * 0.05,
            child: const Text(
              'Engage Smarter, Not Longer',
              style: AppFonts.tagline,
            ),
          ),

          // Video Section
          Container(
            height: MediaQuery.of(context).size.height * 0.2,
            color: AppColors.newColor,
            padding: const EdgeInsets.only(left: 15, right: 15),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              mainAxisSize: MainAxisSize.min, // This makes the container wrap its content
              children: [
                TextField(
                  controller: _urlController,
                  decoration: const InputDecoration(
                    labelText: 'Enter YouTube URL',
                    border: OutlineInputBorder(),
                  ),
                ),
                const SizedBox(height: 10),
                ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.black,
                  ),
                  onPressed: _handleSubmitUrl,
                  child: const Text(
                    'Submit',
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                    ),
                  ),
                ),
              ],
            ),
          ),

          // Summary section
          Container(
            decoration: const BoxDecoration(
                color: Color(0xFF96785B),
              border: Border(
                top: BorderSide(
                  color: Colors.black,
                ),
                bottom: BorderSide(
                  color: Colors.black,
                )
              )
            ),
            height: MediaQuery.of(context).size.height * 0.2,
            padding: const EdgeInsets.all(10),
            child: SingleChildScrollView(
              child: Text(
                _summary,
                style: AppFonts.summaryText,
              ),
            ),
          ),

          // Chat Section
          Expanded(
            child: Container(
              padding: const EdgeInsets.all(10),
              color: AppColors.newColor,
              child: Column(
                children: [
                  // Chat messages
                  Expanded(
                    child: ListView.builder(
                      itemCount: _chatMessages.length,
                      itemBuilder: (context, index) {
                        var message = _chatMessages[index];
                        return ListTile(
                          title: Align(
                            alignment: message["role"] == "user"
                                ? Alignment.centerRight
                                : Alignment.centerLeft,
                            child: Padding(
                              padding: message["role"] == "user"
                                ? EdgeInsets.only(left: 100)
                                : EdgeInsets.only(right: 100),
                              child: Container(
                                padding: EdgeInsets.all(10),
                                color: Color(0xFFECCFA3),
                                // color: message["role"] == "user"
                                //     ? Colors.grey[200]
                                //     : Colors.blue[400],
                                child: Text(
                                  message["message"] ?? '',
                                  style: AppFonts.simpletext,
                                ),
                              ),
                            ),
                          ),
                        );
                      },
                    ),
                  ),

                  // Input row
                  Row(
                    children: [
                      Expanded(
                        child: Container(
                          padding: const EdgeInsets.symmetric(horizontal: 10.0),
                          decoration: BoxDecoration(
                            color: AppColors.newColor, // Background color of the box
                            borderRadius: BorderRadius.circular(8.0), // Rounded corners
                            border: Border.all(
                              color: Colors.grey, // Border color
                              width: 1.0, // Border width
                            ),
                          ),
                          child: TextField(
                            controller: _messageController,
                            decoration: const InputDecoration(
                              hintText: 'Enter your message...',
                              border: InputBorder.none, // Remove the default border
                            ),
                          ),
                        ),
                      ),
                      IconButton(
                        icon: const Icon(Icons.send),
                        onPressed: _handleSendMessage,
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
