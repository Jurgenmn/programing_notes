import React, { Component } from "react";
import { Card, CardImg, CardText, CardBody, CardTitle } from "reactstrap";
//import Col from 'reactstrap/lib/Col';
class CampsiteInfo extends Component {
  renderCampsite(campsite) {
    return (
      <div className="col-md-5 m-1" >
        <Card>
          <CardImg top src={campsite.image} alt={campsite.name} />
          <CardBody>
            <CardTitle>{campsite.name}</CardTitle>
            <CardText>{campsite.description}</CardText>
          </CardBody>
        </Card>
      </div>
    )
  }
  renderComments(comment) {
      if (comment){
          console.log(comment, "what is this ?")
          return (
            <div className='col-md-5 m-1'>
            <h4>Comments</h4>
            {comment.map(comment => {
              const commentDate = new Intl.DateTimeFormat('en-US', { year: 'numeric', month: 'short', day: '2-digit' }).format(new Date(Date.parse(comment.date)))
              return (
                  <div key={comment.id}>
                      <p>
                          {comment.text}<br/>
                            -- {comment.author},{commentDate}
                      </p>
                  </div>
              )
              })}
          </div>
          )
      }
  }

  render() {
    if (this.props.campsite) {
        console.log(this.props.campsite.comments, "grab comments");
      return (
        <div className="row">
            {this.renderCampsite(this.props.campsite)}
            {this.renderComments(this.props.campsite.comments)}
        </div>
      );
    }
    return <div />;
  }
}
export default CampsiteInfo;
