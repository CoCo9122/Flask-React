import React, { useState, useEffect } from "react"
import axios from 'axios'

import { Box, Stack, VStack, HStack, Flex, Text } from '@chakra-ui/react'

const App = () => {

    const [items, setItems] = useState({})

    useEffect(() => {
        axios.get("http://localhost:5000/")
        .then(res => (
            setItems(res.data)
        ))
        .catch(error => console.log(error))
    }, [])

    return(
        <Box>
            <VStack m={3}>
                <Text>Hello React! Good React Life! You must be having fun!</Text>
            </VStack>
            <HStack m={5}>
                <Text pr={10}>item: {items.item}</Text>
                <Text>price: {items.price}</Text>
            </HStack>
        </Box>
    )
}

export default App