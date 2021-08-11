import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:to_do_app/data/data.dart';

import 'add_edit.dart';

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key}) : super(key: key);

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  void didChangeDependencies() {
    // TODO: implement didChangeDependencies
    Provider.of<DataState>(context).getNotesData();
    super.didChangeDependencies();
  }

  @override
  Widget build(BuildContext context) {
    final data = Provider.of<DataState>(context).getNote;
    return Scaffold(
      appBar: AppBar(
        actions: [
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: IconButton(
                onPressed: () =>
                    Navigator.of(context).pushNamed(AddEdit.pageRoute),
                icon: Icon(Icons.add)),
          )
        ],
        title: Text('To do app'),
      ),
      body: Center(
        child: Text('HEllo world'),
      ),
    );
  }
}
