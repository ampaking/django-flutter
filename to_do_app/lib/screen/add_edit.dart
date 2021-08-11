import 'package:flutter/material.dart';

class AddEdit extends StatelessWidget {
  static const String pageRoute = '/add_edit';
  const AddEdit({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        actions: [
          IconButton(
            onPressed: () => Navigator.pop(context),
            icon: Icon(Icons.close),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        backgroundColor: Colors.black,
        onPressed: () {
          Navigator.of(context).pop();
        },
        child: Icon(
          Icons.done_outlined,
          color: Colors.green,
        ),
      ),
      body: Center(
        child: Text('add new note'),
      ),
    );
  }
}
