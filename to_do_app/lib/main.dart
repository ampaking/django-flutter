import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:to_do_app/data/data.dart';
import 'package:to_do_app/screen/add_edit.dart';
import 'package:to_do_app/screen/home_screen.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (ctx) => DataState(),
      child: MaterialApp(
        title: 'Flutter Demo',
        theme: ThemeData(
          primarySwatch: Colors.blue,
        ),
        routes: {
          '/': (ctx) => MyHomePage(),
          AddEdit.pageRoute: (ctx) => AddEdit(),
        },
      ),
    );
  }
}
