import React, { Component } from 'react';
import { ScrollView, Text } from 'react-native';
import { Card } from 'react-native-elements';
import * as Animatable from 'react-native-animatable';


class Contact extends Component {

    static navigationOptions = {
        title: 'Contact US'
    }

    render() {
        return(
            <ScrollView>
                <Animatable.View animation='fadeInDown' duartion={2000} delay={1000}>
                    <Card title="Contact Information" wrapperStyle={{margin: 20}}>
                        <Text>1 Nucamp Way</Text>
                        <Text>Seattle, WA 98001</Text>
                        <Text>U.S.A.</Text>
                        <Text style={{marginBottom: 20}}></Text>
                        <Text>Phone: 1-206-555-1234</Text>
                        <Text>Email: campsites@nucamp.co</Text>
                    </Card>
                </Animatable.View>
            </ScrollView>
        ) 
    }
   
}

export default Contact;