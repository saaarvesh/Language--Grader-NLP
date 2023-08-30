<template>
  <div class="displayGrade">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css">
    <main-pages-header />
    <div class="content">
      <b-card>
        <b-row>
          <b-col md="3">
            <graph-pie
            :height="150"
            :values="values"
            :names="names"
            :active-event="'click'"
            :show-text-type="'outside'"
            :data-format="dataFormat"
            :shape="'donut'">
        <note :text="'Average Score: B'"></note>
        <legends :names="names"></legends>
        <tooltip :names="names"></tooltip>
    </graph-pie>
          </b-col>
          <b-col md="6" class="text-left">
            <h3>Your Total Essay Score:</h3>
            <p>Your total essay score comprises of scores acquired after completing different modules. You can improve you Total Score by editing and fixing mistakes in each module. Follow out Tips to reach better results</p>
          </b-col>
          <b-col md="3" class="text-left" style="border-left:2px solid black">
            <p>
              <strong>Note: </strong>Our grade is a probable mark you can get for your paper, there might be slight difference between the usggested grade and the one professor awards you with because of the human factor which is an integral part of the grading system.
            </p>
          </b-col>
        </b-row>
      </b-card>
      <div class="container">
        <b-row>
          <b-col md="7">
            <b-card>
              <b-card-header>
                <b-row>
                  <b-col md="4" class="text-left">
                    <span>Word count:{{ count }}</span>
                  </b-col>
                  <b-col md="8" class="text-right">
                    <span>Last edited: {{ date }}</span>
                    <b-button class="ml-2" variant="outline-dark"><i class="fa fa-trash-o icon"></i></b-button>
                  </b-col>
                </b-row>
              </b-card-header>
              <b-card-body>
                <b-row class="mt-6">
                  <b-col md="12" class="text-left">
                    <h3>{{ textToGrade.subject }}</h3>
                    <p>{{ textToGrade.text }}</p>
                  </b-col>
                </b-row>
              </b-card-body>
            </b-card>
          </b-col>
          <b-col md="5">
            <b-card>
              <b-card-header>
                <i class="fa fa-commenting-o icon"></i>Feedback Result
              </b-card-header>
              <b-card-body>
                <div class="row single-row">
                  <div class="col-6 text-left single-row">
                    Spelling error
                  </div>
                  <div class="col-6 text-right single-row">
                    10%
                  </div>
                </div>
                <div class="row single-row">
                  <div class="col-6 text-left single-row">
                    Word Repetition
                  </div>
                  <div class="col-6 text-right single-row">
                    5%
                  </div>
                </div>
                <div class="row single-row">
                  <div class="col-6 text-left single-row">
                    Redundunt words
                  </div>
                  <div class="col-6 text-right single-row">
                    5%
                  </div>
                </div>
                <div class="row single-row">
                  <div class="col-6 text-left single-row">
                    Readability
                  </div>
                  <div class="col-6 text-right single-row">
                    5%
                  </div>
                </div>
              </b-card-body>
            </b-card>
          </b-col>
        </b-row>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import MainPagesHeader from '@/components/MainPagesHeader.vue'
import GraphLine3D from 'vue-graph/src/components/line3d.js'
import NoteWidget from 'vue-graph/src/widgets/note.js'
import LegendWidget from 'vue-graph/src/widgets/legends.js'
import GraphPie from 'vue-graph/src/components/pie.js'

Vue.component(GraphLine3D.name, GraphLine3D)
Vue.component(NoteWidget.name, NoteWidget)
Vue.component(LegendWidget.name, LegendWidget)

export default {
  data: function () {
    return (
      {
        values: [10, 5, 5, 5],
        names: ['Spelling error', 'Word Repetition', 'Redundunt words', 'Readability'],
        count: 105,
        date: '31/05/2020',
        textToGrade: {
          subject: 'Hello World',
          text: 'Cows are considered to be a sacred animal in the Hindu religion. The ardent followers of religion worship this animal like a Goddess. A cow has been honored with the status of a mother in Hinduism. This is why people refer to it as ‘Gau Mata’ which translates to Mother Cow. Many followers of religion consider it a sin to kill cows. Nowadays, India has a lot of organizations with the sole purpose of protecting cows. They work to help cows from any danger. They do not tolerate any kind of harm to cows.The government is also taking a lot of measures to protect cows from any injustice. People are coming forward in alliance to safeguard them. They do not prefer any kind of inappropriate behavior with cows. We must work together to protect cows and become the voice for the unspoken.'
        }
      }
    )
  },
  methods: {
    dataFormat: function (a, b) {
      if (b) return b + '%'
      return a
    }
  },
  components: {
    MainPagesHeader,
    GraphPie
  }
}
</script>

<style>
body {
  background-color: grey;
}
.content {
  margin: 150px 30px 150px 30px;
}
.displayGrade .container {
  margin-top: 16px;
}
.col-md-7 {
  padding: 0 0 0 0;
}
.single-row {
  margin: 8px 0;
}
legends {
  margin-top: 50px;
}
</style>
