import React, { Component } from 'react'
import {
  Map,
  TileLayer,
  Marker,
  Popup,
  LayersControl,
  ZoomControl,
  LayerGroup,
  GeoJSON
} from 'react-leaflet'
import 'leaflet/dist/leaflet.css'
import L from 'leaflet'
import { MarkerTypes } from './utils/markerUtils.js' // TODO: determine how we're going to store types
//import { occupied } from './geojson/occupied.js' // TODO: determine how we're going to store geojson
//import { vacant } from './geojson/vacant.js'
import { grocery } from './geojson/grocery.js'
const { Overlay } = LayersControl
// default pins weren't working, so here's a hack from github
delete L.Icon.Default.prototype._getIconUrl
L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png')
})

export default class StlMap extends Component {
  state = {
    center: [38.65, -90.4],
    zoom: 12,
    types: MarkerTypes,
    geojson: {grocery} // TODO: mongo docs
  }

  render () {
    const { center, zoom } = this.state

    return (
      <Map center={center} zoom={zoom} zoomControl={false}>
        <TileLayer
          attribution="&copy; <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
          url="https://tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png"
        />
        <LayersControl position="topright">
          <LayersControl.Overlay name="Layer 1">
            <GeoJSON data={this.state.geojson['grocery']} />
          </LayersControl.Overlay>
        </LayersControl>
        <ZoomControl position='bottomright' />
      </Map>
    )
  }
}
