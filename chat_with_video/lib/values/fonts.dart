import 'package:flutter/material.dart';
import 'package:chat_with_video/values/colors.dart';

class AppFonts {
  static const TextStyle appbarhead = TextStyle(
    color: AppColors.primaryColor,
    fontWeight: FontWeight.w500,
    fontSize: 20,
  );

  static const TextStyle tagline = TextStyle(
    fontFamily: 'Robo',
    fontSize: 17,
    color: AppColors.primaryColor,
    fontWeight: FontWeight.w500,
  );

  static const TextStyle simpletext = TextStyle(
    fontFamily: 'Robo',
    fontSize: 14.0,
    color: Color(0xFF5C433C),
    fontWeight: FontWeight.w500,
  );

  static const TextStyle summaryText = TextStyle(
    fontFamily: 'Robo',
    fontSize: 14,
    fontWeight: FontWeight.w500,
    color: Colors.white,
  );
}
